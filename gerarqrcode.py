import qrcode

# Dados que você quer codificar no QR code
dados = "https://www.instagram.com/dnaraujo11/"

# Cria o objeto QR code
qr = qrcode.QRCode(
    version=1,  # Tamanho do QR code (1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # Nível de correção de erros
    box_size=10, # Tamanho de cada "caixa" do QR code
    border=4, # Largura da borda do QR code
)

# Adiciona os dados ao QR code
qr.add_data(dados)
qr.make(fit=True)

# Cria a imagem do QR code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem do QR code
img.save("qrcode.png") # Linha corrigida

print("QR code gerado com sucesso!")