# Machine Learning Spring 2025 Kaggle Competition 2


- 임도협(24101518)
- 원송원(24102401)


**Train and Predict:**
```bash
python main.py
```

**Precompute Features:**
```bash
python main.py --precompute
```


# Dataset Description

## 제공되는 파일 📁
- train/ (폴더)

  모델 학습에 사용되는 .wav 형식의 오디오 파일들이 담겨 있습니다. 각 파일은 한 사람의 호흡 소리(들숨 또는 날숨)를 담고 있습니다.

- test/ (폴더)

  모델 성능 평가에 사용되는 .wav 형식의 오디오 파일들이 담겨 있습니다. 이 파일들에 대해 들숨/날숨을 예측해야 합니다.

- train.csv

  학습 세트 정보 파일입니다. train/ 폴더의 오디오 파일들에 대한 정답 레이블을 포함합니다. 이 파일을 사용하여 모델을 학습시킬 수 있습니다.

- test.csv

  테스트 세트 정보 파일입니다. 여러분이 예측해야 할 test/ 폴더 안의 오디오 파일들의 ID 목록입니다. 이 파일에 있는 모든 ID에 대해 예측값을 제출해야 합니다.

## 데이터 열(Columns) 설명 📝

- train.csv

  - file_name: 오디오 파일의 고유 식별자(파일 이름)입니다. train/ 폴더의 .wav 파일과 일치합니다.
  - label: 해당 오디오 파일의 정답 레이블입니다.
    - I: 들숨 (Inhale)
    - E: 날숨 (Exhale)

- test.csv
  - ID: 예측해야 할 오디오 파일의 고유 식별자입니다.
 
