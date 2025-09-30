from math import radians, sin, cos, tan

a = radians(float(input('Digite um ângulo: ')))

print("""
* Seno: {:.2f}
* Cosseno: {:.2f}
* Tangente: {:.2f}
""".format(sin(a), cos(a), tan(a))
)