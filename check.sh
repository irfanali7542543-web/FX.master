#!/bin/bash
echo "--- FX-MASTER کوڈ کی جانچ پڑتال ---"
flake8 monitor.py > error.txt
if [ -s error.txt ]; then
    echo "❌ غلطی ملی! تفصیل نیچے دیکھیں:"
    cat error.txt
else
    echo "✅ زبردست! کوڈ بالکل ٹھیک ہے، کوئی غلطی نہیں ملی۔"
fi
rm error.txt
