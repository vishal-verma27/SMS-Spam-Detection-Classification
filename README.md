# SMS-Spam-Detection-Classification-99%-Accurate

Pre-trained model to classify a message as 'ham' or 'spam' along with confidence level

*This model can classify a given text sms as spam or ham along with level of confidence.*

Get Predictions-

**base_URL/smsPredict/Your_SMS_TEXT**

## For Example-

### Sample 1

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

### Sample 2

**Input**

**base_URL/smsPredict/Hi How are you**

**Output**

{
  "confidence": {
    "ham": 0.9989423958666416,
    "spam": 0.0010576041333586641
  },
  "input_text": "Hi How are you",
  "pred_label": "ham"
}
