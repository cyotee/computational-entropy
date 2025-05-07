
# Decay Vector Representation in Encryption Scenarios

## Introduction

This document explores the application of the decay vector concept to encryption scenarios. The decay vector, denoted as \( ([d_1, d_2, \ldots, d_{n(f)}], d_f) \), is a metric that quantifies the recoverability of input variables and the identifiability of a function based on its output. In this context, we use it to represent cases where a result (e.g., ciphertext) maps uniquely to a specific input value (e.g., encryption key), yet the key remains unrecoverable due to cryptographic design. Here, \( d_i = 0 \) if the \( i \)-th input is recoverable from the output, and \( d_i = 1 \) if it is not.

## Encryption Scenario

Consider an encryption function \( f(\text{key}, \text{plaintext}) = \text{ciphertext} \), where the ciphertext depends uniquely on both the key and the plaintext. In a secure encryption system:

- The ciphertext could theoretically correspond to a specific key for a given plaintext.
- However, cryptographic principles ensure that recovering the key from the ciphertext is computationally infeasible without additional information, even with access to multiple input-output pairs.

This scenario highlights a distinction between theoretical uniqueness and practical recoverability.

## Applying the Decay Vector

### Standard Decay Vector Interpretation

In the context of encryption, the decay vector is applied as follows:

- \( d_{\text{key}} = 1 \): The key cannot be uniquely recovered from the ciphertext alone due to the one-way nature of the encryption function.
- \( d_{\text{plaintext}} = 1 \): The plaintext cannot be recovered without the key, aligning with the security goals of encryption.
- **Result**: \( [1, 1] \)

This \( [1, 1] \) decay vector reflects that neither input (key nor plaintext) is determinable from the output alone, a fundamental requirement for secure encryption.

### Theoretical vs. Practical Recoverability

- **Theoretical Perspective**: If the encryption function is bijective for a fixed plaintext (i.e., each ciphertext corresponds to exactly one key), the key could theoretically be determined with sufficient data and computational power.
- **Practical Perspective**: Modern cryptographic systems, such as AES or RSA, are designed to make key recovery computationally infeasible, even if the mapping is theoretically unique.

The decay vector emphasizes theoretical recoverability. However, in this encryption context, we assign \( d_{\text{key}} = 1 \) and \( d_{\text{plaintext}} = 1 \) to reflect the practical security constraint that neither input can be feasibly recovered from the ciphertext alone.

## Conclusion

In encryption scenarios where the ciphertext maps uniquely to a key for a given plaintext, yet the key remains practically unrecoverable, the decay vector is represented as \( [1, 1] \). This representation encapsulates the core principle of secure encryption: obscuring input information to prevent recovery from the output. The decay vector thus serves as a useful tool for analyzing the information preservation—or intentional loss—within cryptographic systems.


# Decay Vector Representation in Encryption Scenarios

## Introduction
This document explores the application of the decay vector concept to encryption scenarios. The decay vector, denoted as \( ([d_1, d_2, \ldots, d_{n(f)}], d_f) \), is a metric that quantifies the recoverability of input variables and the identifiability of a function based on its output. In this context, we use it to represent cases where a result (e.g., ciphertext) maps uniquely to a specific input value (e.g., encryption key), yet the key remains unrecoverable due to cryptographic design. Here, \( d_i = 0 \) if the \( i \)-th input is recoverable from the output, and \( d_i = 1 \) if it is not.

## Encryption Scenario
Consider an encryption function \( f(\text{key}, \text{plaintext}) = \text{ciphertext} \), where the ciphertext depends uniquely on both the key and the plaintext. In a secure encryption system:
- The ciphertext could theoretically correspond to a specific key for a given plaintext.
- However, cryptographic principles ensure that recovering the key from the ciphertext is computationally infeasible without additional information, even with access to multiple input-output pairs.

This scenario highlights a distinction between theoretical uniqueness and practical recoverability.

## Applying the Decay Vector
### Standard Decay Vector Interpretation
In the context of encryption, the decay vector is applied as follows:
- \( d_{\text{key}} = 1 \): The key cannot be uniquely recovered from the ciphertext alone due to the one-way nature of the encryption function.
- \( d_{\text{plaintext}} = 1 \): The plaintext cannot be recovered without the key, aligning with the security goals of encryption.
- **Result**: \( [1, 1] \)

This \( [1, 1] \) decay vector reflects that neither input (key nor plaintext) is determinable from the output alone, a fundamental requirement for secure encryption.

### Theoretical vs. Practical Recoverability
- **Theoretical Perspective**: If the encryption function is bijective for a fixed plaintext (i.e., each ciphertext corresponds to exactly one key), the key could theoretically be determined with sufficient data and computational power.
- **Practical Perspective**: Modern cryptographic systems, such as AES or RSA, are designed to make key recovery computationally infeasible, even if the mapping is theoretically unique.

The decay vector emphasizes theoretical recoverability. However, in this encryption context, we assign \( d_{\text{key}} = 1 \) and \( d_{\text{plaintext}} = 1 \) to reflect the practical security constraint that neither input can be feasibly recovered from the ciphertext alone.

## Conclusion
In encryption scenarios where the ciphertext maps uniquely to a key for a given plaintext, yet the key remains practically unrecoverable, the decay vector is represented as \( [1, 1] \). This representation encapsulates the core principle of secure encryption: obscuring input information to prevent recovery from the output. The decay vector thus serves as a useful tool for analyzing the information preservation—or intentional loss—within cryptographic systems.