import streamlit as st

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def app():
    st.title('Prime and Composite Numbers from 1 to 50')

    primes = [n for n in range(1, 51) if is_prime(n)]
    composites = [n for n in range(1, 51) if not is_prime(n) and n != 1]

    st.write('## Prime Numbers')
    st.write(primes)

    st.write('## Composite Numbers')
    st.write(composites)

if __name__ == '__main__':
    app()
import streamlit as st

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def app():
    st.title('Prime and Composite Numbers from 1 to 50')

    primes = [n for n in range(1, 51) if is_prime(n)]
    composites = [n for n in range(1, 51) if not is_prime(n) and n != 1]

    st.write('## Prime Numbers')
    st.write(primes)

    st.write('## Composite Numbers')
    st.write(composites)

if __name__ == '__main__':
    app()
import streamlit as st

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def app():
    st.title('Prime and Composite Numbers from 1 to 50')

    primes = [n for n in range(1, 51) if is_prime(n)]
    composites = [n for n in range(1, 51) if not is_prime(n) and n != 1]

    st.write('## Prime Numbers')
    st.write(primes)

    st.write('## Composite Numbers')
    st.write(composites)

if __name__ == '__main__':
    app()
