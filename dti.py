import streamlit as st
import random
import time

# ---------- Stress Calculation ----------
def detect_stress(pulse, temperature):
    if pulse > 110 or temperature > 37.8:
        return "High Stress", "red"
    elif pulse > 90:
        return "Stress", "orange"
    elif pulse > 75:
        return "Normal", "yellow"
    else:
        return "Calm", "green"


# ---------- Streamlit Page Setup ----------
st.set_page_config(
    page_title="HeartSync Ring",
    page_icon="💗",
    layout="centered",
)


st.title("💗 HeartSync Ring – Wellness Dashboard")
st.write("Emotion-linked digital wellness system")


# ---------- Simulated Sensor Data ----------
if "pulse" not in st.session_state:
    st.session_state.pulse = random.randint(60, 90)
if "temp" not in st.session_state:
    st.session_state.temp = round(random.uniform(36.0, 37.0), 1)


# Button to update simulated data
if st.button("🔄 Refresh Data"):
    st.session_state.pulse = random.randint(60, 130)
    st.session_state.temp = round(random.uniform(36.0, 38.5), 1)
    st.experimental_rerun()


pulse = st.session_state.pulse
temperature = st.session_state.temp

stress_state, color = detect_stress(pulse, temperature)


# ---------- Display UI Panels ----------
st.subheader("📊 Live Bio-Signals")

st.metric("❤️ Pulse", f"{pulse} bpm")
st.metric("🌡️ Temperature", f"{temperature} °C")

st.markdown(f"""
### 🧠 Stress Level: <span style='color:{color}; font-size:24px;'>
**{stress_state}**
</span>
""", unsafe_allow_html=True)


# ---------- AI Insights ----------
st.subheader("🤖 Wellness Insights")

if stress_state == "High Stress":
    st.error("Your stress is high. It's recommended to take a break, breathe slowly, or step away from screens.")
elif stress_state == "Stress":
    st.warning("You might be feeling overwhelmed. Reduce screen time and drink some water.")
elif stress_state == "Normal":
    st.info("Everything looks stable. Maintain your balance and continue your activity.")
else:
    st.success("You are calm and relaxed. Great job!")


# ---------- Footer ----------
st.markdown("---")
st.caption("HeartSync Ring – Smart Emotional Wellness System")
