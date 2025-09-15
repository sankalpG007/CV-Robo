from abc import ABC, abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def process_payment(self, amount):
        pass
    @abstractmethod
    def generate_receipt(self):
        pass
    def complete_transaction(self, amount):
        self.authenticate()
        result = self.process_payment(amount)
        receipt = self.generate_receipt()
        return f"{result}\n{receipt}"
class CreditCardProcessor(PaymentProcessor):
    def authenticate(self):
        return "Card authenticated via 3D Secure"
    
    def process_payment(self, amount):
        return f"Processed ${amount} via Credit Card"
    
    def generate_receipt(self):
        return "Receipt: Credit Card Transaction #12345"

processor = CreditCardProcessor()
print(processor.complete_transaction(150))