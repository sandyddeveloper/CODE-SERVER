Here's the complete folder structure for integrating **Razorpay, Google Pay, UPI, and PhonePe** in a Django backend and React frontend project.

---

# **Folder Structure**

### **Backend (Django)**
```
payment_project/
├── payment_project/         # Main project folder
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URLs
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
├── payments/                # Payments app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/          # Database migrations
│   │   └── __init__.py
│   ├── models.py            # For payment-related models if needed
│   ├── views.py             # Payment-related views
│   ├── urls.py              # App-specific URLs
│   └── tests.py             # Unit tests for payments
├── manage.py                # Django CLI
└── requirements.txt         # Python dependencies
```

### **Frontend (React)**
```
payment-frontend/
├── public/
│   ├── index.html           # Main HTML file
│   └── ...
├── src/
│   ├── components/          # React components
│   │   ├── RazorpayPayment.js  # Razorpay payment button
│   │   ├── GooglePayButton.js  # Google Pay button
│   │   └── UpiQrCode.js        # UPI QR Code generation
│   ├── App.js               # Main React app
│   ├── index.js             # React DOM entry point
│   └── api/                 # API request handlers
│       ├── razorpay.js      # Axios calls for Razorpay
│       └── phonepe.js       # Axios calls for PhonePe
├── package.json             # Node.js dependencies
└── .env                     # Environment variables (e.g., API keys)
```

---

# **Detailed Explanation of Folder Structure**

### **Backend: Django**
- **`payment_project/`**:
  - Contains the main Django project files.
  - `settings.py`: Configure Razorpay credentials, database, and installed apps.
  - `urls.py`: Root-level URL configuration.

- **`payments/`**:
  - Dedicated app for payment-related logic.
  - `views.py`: Contains the logic for creating orders and verifying payments for Razorpay, Google Pay, etc.
  - `urls.py`: App-level URL routing for endpoints like `create_order/` and `verify_payment/`.

- **`migrations/`**:
  - Auto-generated files for database schema changes.

- **`requirements.txt`**:
  - Lists dependencies:
    ```txt
    django
    djangorestframework
    django-cors-headers
    razorpay
    requests
    ```

---

### **Frontend: React**
- **`components/`**:
  - Reusable components for different payment gateways:
    - `RazorpayPayment.js`: Implements Razorpay checkout.
    - `GooglePayButton.js`: Implements Google Pay integration.
    - `UpiQrCode.js`: Dynamically generates UPI QR codes.

- **`api/`**:
  - Centralized API handlers using Axios:
    - `razorpay.js`: Handles communication with Django's Razorpay endpoints.
    - `phonepe.js`: Handles PhonePe payment requests.

- **`App.js`**:
  - Main application entry point. Includes buttons or forms to initiate different payment methods.

- **`.env`**:
  - Stores sensitive environment variables, e.g.:
    ```
    REACT_APP_RAZORPAY_KEY=your_razorpay_key
    REACT_APP_API_BASE_URL=http://127.0.0.1:8000
    ```

---

# **File Details and Key Code**

### **Backend: Key Files**
1. **`payments/views.py`**:
   Handles Razorpay payment logic:
   ```python
   import razorpay
   from django.http import JsonResponse
   from django.views.decorators.csrf import csrf_exempt
   import json

   client = razorpay.Client(auth=("YOUR_KEY_ID", "YOUR_SECRET_KEY"))

   @csrf_exempt
   def create_order(request):
       data = json.loads(request.body)
       order = client.order.create({
           "amount": int(data["amount"]) * 100,
           "currency": "INR",
           "payment_capture": 1,
       })
       return JsonResponse(order)

   @csrf_exempt
   def verify_payment(request):
       data = json.loads(request.body)
       try:
           client.utility.verify_payment_signature(data)
           return JsonResponse({"status": "Payment Verified"})
       except razorpay.errors.SignatureVerificationError:
           return JsonResponse({"status": "Payment Verification Failed"}, status=400)
   ```

2. **`payments/urls.py`**:
   ```python
   from django.urls import path
   from .views import create_order, verify_payment

   urlpatterns = [
       path('create_order/', create_order, name='create_order'),
       path('verify_payment/', verify_payment, name='verify_payment'),
   ]
   ```

---

### **Frontend: Key Files**
1. **`src/components/RazorpayPayment.js`**:
   ```jsx
   import React from "react";
   import axios from "axios";

   const RazorpayPayment = () => {
       const handlePayment = async () => {
           const { data } = await axios.post("http://127.0.0.1:8000/payments/create_order/", {
               amount: 500,
           });

           const options = {
               key: data.key_id,
               amount: data.amount,
               currency: data.currency,
               name: "Test Transaction",
               order_id: data.id,
               handler: async (response) => {
                   const verification = await axios.post(
                       "http://127.0.0.1:8000/payments/verify_payment/",
                       response
                   );
                   alert(verification.data.status);
               },
           };

           const razorpay = new window.Razorpay(options);
           razorpay.open();
       };

       return <button onClick={handlePayment}>Pay with Razorpay</button>;
   };

   export default RazorpayPayment;
   ```

2. **`src/components/GooglePayButton.js`**:
   ```jsx
   import React from "react";

   const GooglePayButton = () => {
       const handleGooglePay = () => {
           const paymentsClient = new window.google.payments.api.PaymentsClient({ environment: "TEST" });

           const paymentDataRequest = {
               apiVersion: 2,
               apiVersionMinor: 0,
               allowedPaymentMethods: [
                   {
                       type: "CARD",
                       parameters: {
                           allowedAuthMethods: ["PAN_ONLY", "CRYPTOGRAM_3DS"],
                           allowedCardNetworks: ["VISA", "MASTERCARD"],
                       },
                       tokenizationSpecification: {
                           type: "PAYMENT_GATEWAY",
                           parameters: { gateway: "razorpay" },
                       },
                   },
               ],
           };

           paymentsClient.loadPaymentData(paymentDataRequest).then((paymentData) => {
               console.log(paymentData);
               alert("Payment Successful!");
           });
       };

       return <button onClick={handleGooglePay}>Pay with Google Pay</button>;
   };

   export default GooglePayButton;
   ```



