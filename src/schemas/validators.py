import re
from datetime import date

# Variáveis de Domínio e Segurança
MIN_BIRTH_DATE = date(1876,1,1)

PASSWORD_PATTERN = {
    "uppercase": (r'[A-Z]', "uma letra maiúscula"),
    "lowercase": (r'[a-z]', "uma letra minúscula"),
    "digit": (r'\d', "um número"),
    "special": (r'[!@#$%^&*(),.?":{}|<>]', "um caractere especial"),
}

def validate_password(v: str) -> str:
        if v is None:
            return v

        errors = []
        for _, (pattern, message) in PASSWORD_PATTERN.items():
            if not re.search(pattern, v):
                errors.append(message)
        
        if errors:
            raise ValueError(f"A senha deve conter pelo menos: {', '.join(errors)}.")