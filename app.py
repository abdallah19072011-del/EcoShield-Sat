import tkinter as tk
from tkinter import messagebox

def check_climate_alert():
    # بيانات محاكاة لقراءة ناسا الحية
    temp = 24.9
    humidity = 56.7
    heat_index = 25.9
    
    result_text.set(f"درجة الحرارة: {temp} مئوية\nالرطوبة: {humidity}%\nمؤشر الحرارة: {heat_index} مئوية")
    
    if heat_index > 35.0:
        status_label.config(fg="red")
        status_text.set("⚠️ تحذير خطير: خطر موجة حارة على المحاصيل!")
        messagebox.showwarning("إنذار مبكر - EcoShield-Sat", "تنبيه! مؤشر الحرارة تجاوز الحد الآمن، يرجى تفعيل نظام العزل الحراري!")
    else:
        status_label.config(fg="green")
        status_text.set("✅ آمن: لا يوجد خطر حراري حالياً.")
        messagebox.showinfo("حالة الطقس - EcoShield-Sat", "الحالة آمنة تماماً. المحاصيل في نطاق الأمان.")

root = tk.Tk()
root.title("EcoShield-Sat - نظام الإنذار المبكر للمناخ")
root.geometry("450x350")
root.config(bg="#f0f4f8")

title_label = tk.Label(root, text="🌱 EcoShield-Sat Live Monitor", font=("Arial", 14, "bold"), bg="#f0f4f8", fg="#2c3e50")
title_label.pack(pady=20)

result_text = tk.StringVar()
result_text.set("اضغط على الزر أدناه لبدء فحص قراءات ناسا الحية...")

info_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), bg="white", fg="#34495e", relief="solid", width=40, height=5)
info_label.pack(pady=10)

status_text = tk.StringVar()
status_text.set("الحالة: في انتظار الفحص...")

status_label = tk.Label(root, textvariable=status_text, font=("Arial", 11, "bold"), bg="#f0f4f8")
status_label.pack(pady=10)

btn = tk.Button(root, text="فحص بيانات المناخ الآن", command=check_climate_alert, font=("Arial", 12, "bold"), bg="#27ae60", fg="white", padx=10, pady=5)
btn.pack(pady=15)

root.mainloop()