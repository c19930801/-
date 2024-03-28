while True:
    try:
        he,we=map(float,input().split())
        bmi=we/(((he/100)**2))
        bmi=round(bmi,2)
        print(f"bmi: {bmi}")
    except:
        break