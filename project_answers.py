import number_theory_functions as ntf
import rsa_functions as rsa


def main():
    # riddle 1 answer
    ans1 = "Riddle 1:\n" + \
           "It is possible if Loki gives Iron man 1179 million coins of\n" + \
           "797 USD, and receives a change of 178 million bills of 5279 USD.\n"
    # calculation is done with:
    # ntf.extended_gcd(5279,797)
    print(ans1)

    # riddle 2 answer
    ans2 = "Riddle 2:\n" + \
           "By running the calculation: modular_exponent(23539673, 3434462, 1000)\n" + \
           "we get the result 329, which means the hundred's digit is 3.\n"
    # calculation is done with:
    # ntf.modular_exponent(23539673, 3434462, 1000)
    # giving result of 329, which means the hundreds' digit is 3.
    print(ans2)

    # riddle 3 answer
    # By using other tools, we found that a factorization of 12215009 can be 3491*3499
    # which means we are going to use: p=3491 , q=3499
    p, q = 3491, 3499
    k = (p - 1) * (q - 1)
    N = 12215009
    d = ntf.modular_inverse(q, k)  # d = 5425399
    code = rsa.RSA(public_key=(N, q), private_key=(N, d))
    m = 42
    decrypted_m = code.decrypt(m)

    ans3 = "Riddle 3:\n" + \
           "The decrypted message is: {0}.\n".format(decrypted_m) + \
           "We found it by using other tools to find that a factorization of\n" + \
           "N=12215009 can be p*q=3491*3499. Then we calculated k = phi(N) = (p-1)*(q-1)\n" + \
           "and used this data to find d for the private key, by using modular_inverse(q,k).\n" + \
           "We then initialized an RSA class object with the private key ({0},{1})\n".format(N, d) + \
           "and the public key ({0},{1})\n".format(N, q) + \
           "Finally we decrypted the message m = {0} and got the decryption: {1}.\n".format(m, decrypted_m)
    print(ans3)

    # riddle 4 answer
    p, q = 7919, 6841
    m = 71
    N = p * q
    k = (p - 1) * (q - 1)
    # we used this method calculate e, d once and chose them, because the
    # function uses random numbers but we want our answer to be deterministic.
    # d, e = rsa.RSA.calc_private_and_public(k)
    d, e = 47157973, 820237
    code = rsa.RSA(public_key=(N, e), private_key=(N, d))
    encrypted_message = code.encrypt(m=m)
    decrypted_message = code.decrypt(c=encrypted_message)
    ans4 = "Riddle 4:\n" + \
           "We chose to encrypt the message: m = {0}\n".format(m) + \
           "The public key is: ({0},{1})\n".format(N, e) + \
           "The encrypted message is: {0}\n".format(encrypted_message) + \
           "And by decrypting the encrypted message we get the same message we started with, {0}.\n".format(decrypted_message)
    print(ans4)


if __name__ == "__main__":
    main()
