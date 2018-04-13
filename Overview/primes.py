# # vigane variant
def isprime(n):
    for i in range(n):
        if n % i == 0:
            return False
    
    return True

# # Parandatud variant
# def isprime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# # 0 ja 1 haldamine
# def isprime(n):
#     if n in (0, 1):
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# def isprime(n):
#     if n < 0:
#         return False

#     if n in (0, 1):
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True

# # Lõplik versioon
# def isprime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# # Kustume funktsiooni testimiseks välja
# n = 5
# if isprime(n):
#     print(f"{n} ON algarv")  # Kasutame f-formaatimisstringi, mis lubab muutuja otse stringi sisse panna
# else:
#     print(f"{n} EI OLE algarv")


# def list_primes(max_num = 100):
#     for n in range(2, max_num):
#         if isprime(n):
#             print(n, end = ' ', flush = True)
#     print()

# list_primes()