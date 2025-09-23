# app.py (auto-load model without upload prompt)
import streamlit as st
import pandas as pd
import numpy as np
import pickle, joblib, os

# ----------------- Page -----------------
st.set_page_config(page_title="Placement Predictor", layout="centered")
st.title("Placement Predictor — The Mole & The Byte")
st.caption("App auto-loads model.pkl. Place model.pkl in this folder or adjust PREFERRED_PATHS.")

# ----------------- Config -----------------
FEATURES = [
    "IQ",
    "Prev_Sem_Result",
    "CGPA",
    "Academic_Performance",
    "Internship_Experience",
    "Extra Curricular_Score",
    "Communication_Skills",
    "Projects_Completed"
]
TARGET = "Placement"
BINARY_YN = ["Internship_Experience"]

# ----------------- Model loader (auto) -----------------
PREFERRED_PATHS = [
    "model.pkl",  # same folder
    os.path.join("import_pickle_model", "model.pkl"),  # common subfolder you mentioned
    r"E:\machine learning\model.pkl",  # your full path (adjust if needed)
    r"E:\machine learning\import_pickle_model\model.pkl"
]

@st.cache_resource
def try_load(paths):
    last_exc = None
    for p in paths:
        if p and os.path.exists(p):
            try:
                with open(p, "rb") as f:
                    return pickle.load(f)
            except Exception:
                try:
                    return joblib.load(p)
                except Exception as e:
                    last_exc = e
    if last_exc is not None:
        raise last_exc
    raise FileNotFoundError("No model file found in preferred paths: " + ", ".join(paths))

model = None
try:
    model = try_load(PREFERRED_PATHS)
    st.success("Loaded model from disk.")
except FileNotFoundError:
    st.error("model.pkl not found. Place model.pkl in the same folder as app.py or update PREFERRED_PATHS.")
except Exception as e:
    st.error(f"Error while loading model: {e}")

# ----------------- Helpers -----------------
def map_yesno_series(s):
    return s.map({"Yes":1,"No":0,"yes":1,"no":0,"YES":1,"NO":0}).fillna(s).astype(float)

def validate_and_align(df: pd.DataFrame):
    for col in BINARY_YN:
        if col in df.columns:
            df[col] = map_yesno_series(df[col])
    if TARGET in df.columns:
        df[TARGET] = map_yesno_series(df[TARGET])
    missing = [c for c in FEATURES if c not in df.columns]
    if missing:
        st.warning(f"Missing columns {missing} - filling with 0s.")
        for m in missing:
            df[m] = 0
    df = df[FEATURES].astype(float)
    return df

def map_to_label(y):
    arr = np.array(y).ravel()
    out = []
    for v in arr:
        try:
            fv = float(v)
            if 0.0 <= fv <= 1.0 and not fv.is_integer():
                out.append("Yes" if fv >= 0.5 else "No")
            else:
                out.append("Yes" if int(round(fv)) == 1 else "No")
        except Exception:
            out.append(str(v))
    return out

# ----------------- UI: example filler & single prediction -----------------
if st.button("Fill example values"):
    st.session_state.update({
        "IQ": 120,
        "Prev_Sem_Result": 6.5,
        "CGPA": 8.0,
        "Academic_Performance": 8,
        "Internship_Experience": 1,
        "Extra Curricular_Score": 6,
        "Communication_Skills": 7,
        "Projects_Completed": 2
    })

st.markdown("### Manual input (single prediction)")
with st.form("single_form"):
    cols = st.columns(2)
    inputs = {}
    for i, feat in enumerate(FEATURES):
        with cols[i % 2]:
            if feat in BINARY_YN:
                inputs[feat] = st.radio(
                    feat,
                    options=[0, 1],
                    index=0 if float(st.session_state.get(feat, 0)) == 0 else 1,
                    format_func=lambda x: "Yes" if x == 1 else "No"
                )
            else:
                if feat in ["Academic_Performance", "Extra Curricular_Score", "Communication_Skills", "Projects_Completed"]:
                    inputs[feat] = st.number_input(feat, value=float(st.session_state.get(feat, 0.0)), step=1.0)
                else:
                    inputs[feat] = st.number_input(feat, value=float(st.session_state.get(feat, 0.0)))
    submit = st.form_submit_button("Predict single")

if submit:
    if model is None:
        st.error("Model not loaded. Place model.pkl in the same folder as app.py (or edit PREFERRED_PATHS).")
    else:
        X = pd.DataFrame([inputs], columns=FEATURES)
        X = validate_and_align(X)
        try:
            pred = model.predict(X.values)
            labels = map_to_label(pred)
            st.success(f"Prediction: {labels[0]}")
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(X.values)
                st.write("Probabilities (per class):", proba[0].tolist())
        except Exception as e:
            st.error(f"Prediction error: {e}")

# ----------------- Batch CSV uploader (keeps CSV functionality but no model upload) -----------------
st.markdown("### Or upload CSV for batch predictions")
uploaded = st.file_uploader("Upload CSV (must contain these columns): " + ", ".join(FEATURES), type=["csv"])
if uploaded is not None:
    if model is None:
        st.error("Model not loaded. Place model.pkl in folder or update PREFERRED_PATHS.")
    else:
        try:
            df = pd.read_csv(uploaded)
            df_proc = validate_and_align(df.copy())
            preds = model.predict(df_proc.values)
            labels = map_to_label(preds)
            df["Prediction"] = labels
            st.success("Batch predictions added (column: Prediction). Preview:")
            st.dataframe(df.head(20))
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download predictions CSV", data=csv, file_name="predictions_with_predictions.csv")
        except Exception as e:
            st.error(f"Batch prediction error: {e}")

# ----------------- Notes -----------------
st.markdown(
    """
**Notes**
- This app will NOT prompt for model upload. It auto-loads model.pkl from the current folder or PREFERRED_PATHS.
- If you still see "model not loaded" put your model file at one of these paths or update PREFERRED_PATHS at top of this file.
"""
)
