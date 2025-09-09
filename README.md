
# 📊 Monte Carlo Simulation of Gaussian Distribution PDF

This project uses the **accept–reject Monte Carlo method** to generate Gaussian-distributed random numbers and estimate the probability distribution function (PDF).

---

## 📂 Code Structure
- **main.py** → accept–reject algorithm + histogram plotting.

---

## 🔑 Important Variables
- `N` → number of generated samples  
- `peak` → Gaussian maximum (normalization constant)  
- `r` → sampling range for uniform random numbers  

---

## ⚙️ How to Interact
1. Open **main.py**  
2. Adjust `N` to increase or decrease the number of samples.  
3. Modify `r` to change the domain of sampling.  
4. Run:
   ```bash
   python main.py

---

## 🧠 Physical/Statistical Intuition

* As `N` grows, the histogram converges toward a Gaussian curve.

* The Gaussian distribution has the form:

  $$
  P(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-x^2 / 2\sigma^2}
  $$

* Demonstrates how uniform random numbers can be transformed into a non-uniform Gaussian PDF.

---

## 🧮 Numerical Models

* **Accept–Reject Monte Carlo**
* **Probability distribution function (PDF) estimation**
* **Law of Large Numbers**


