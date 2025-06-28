import streamlit as st

st.set_page_config(page_title="🚦 برج المراقبة الذكي", page_icon="🚗", layout="centered")


st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
    }
    .big-title {
        font-size:36px;
        color:#2c3e50;
        font-weight:bold;
        text-align:center;
        margin-bottom:20px;
    }
    .footer {
        text-align:center;
        font-size:14px;
        color:#888;
        margin-top:50px;
    }
    </style>
""", unsafe_allow_html=True)

# 🔥 العنوان الكبير مع الشعار
st.markdown('<div class="big-title">🚦 برج المراقبة الذكي</div>', unsafe_allow_html=True)

st.write("""
هذا النظام يحاكي عمل برج مراقبة ذكي يراقب السرعة والمسافات بين المركبات
لإصدار تنبيهات لتقليل الحوادث وحماية الأرواح.
""")

# مدخلات المستخدم
speed = st.number_input("🚗 ما سرعتك الحالية؟ (كم/ساعة)", min_value=0, step=1)
distance = st.number_input("🚙 كم المسافة بينك وبين السيارة أمامك؟ (متر)", min_value=0, step=1)

# زر تنفيذ
if st.button("تحقق الآن 🚦"):
    if speed == 0 or distance == 0:
        st.warning("يرجى إدخال السرعة والمسافة أولًا.")
    else:
        safe_distance = speed / 2
        if distance >= safe_distance + 5:
            st.success("✅ كل شيء آمن، استمر في القيادة بحذر.")
        elif distance >= safe_distance:
            st.info("⚠ الوضع مقبول لكن حاول زيادة المسافة قليلًا.")
        else:
            st.error("🚨 خطر! المسافة قصيرة جدًا بالنسبة لسرعتك. يرجى تخفيف السرعة فورًا.")

# هامش معلوماتي
st.markdown("""
---
📊 هل تعلم؟  
حوالي 30% من الحوادث سببها عدم ترك مسافة أمان كافية بين المركبات.
""")

# Footer
st.markdown('<div class="footer">🚀 تم تطوير هذا المشروع باستخدام Python + Streamlit</div>', unsafe_allow_html=True)