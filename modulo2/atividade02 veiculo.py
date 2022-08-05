rodas = int(input("quantas rodas tem o veículo?"))
peso = float(input("qual peso bruto em Quilograma do veiculo?"))
pessoas = int(input("quantas pessoas cabem no veículo?"))
if (rodas>1 and rodas<4):
	print("Veículo da Categoria A")
elif (rodas >3) and (pessoas <9) and (peso < 35000):
	print("Veiculo da Categoria B")
elif (rodas >3) and (peso > 35000) and (peso <60000):
	print("Veiculo da Categoria C")
elif (rodas >3) and (pessoas >8):
	print("Veiculo da Categoria D")
else: 
	print("Veiculo da Categoria E") 
