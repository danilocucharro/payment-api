import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # Will simulate a payment_id received from the bank
        bank_payment_id = str(uuid.uuid4())

        hash_payment = f'hash_payment_{bank_payment_id}' #it could be received from the bank

        # Creating and saving the qrcode img
        img = qrcode.make(hash_payment)
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")

        return {
                "bank_payment_id": bank_payment_id,
                "qr_code_path": f"qr_code_payment_{bank_payment_id}"
            }