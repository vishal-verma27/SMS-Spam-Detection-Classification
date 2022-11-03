# SMS-Spam-Detection-Classification
Pre-trained model to classify a message as 'ham' or 'spam' along with confidence level

Get Predictions-

**base_URL/smsPredict/Your_SMS_TEXT**

# For Example-

**Input**

**base_URL/smsPredict/claim your free gift worth $200**

**Output**

{
  "confidence": {
    "ham": 2.6515678832805816e-06,
    "spam": 0.9999973484321156
  },
  "input_text": "claim your free gift worth $200",
  "pred_label": "spam"
}
