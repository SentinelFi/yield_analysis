# Flight-Delay Insurance Underwriting Report

## 1. Introduction  
In this model, 
* an investor collects a **premium** (π) for each flight-delay policy sold.  
* If a flight is **delayed**, the investor pays a **payout** (λ).  
* he probability of delay, *p*, varies from **1% to 20%**.  

This report estimates how **yield** changes when adjusting premium, payout, the number of policies (*M*), and initial capital (*C*).

---

## 2. Yield Formula  
The investor’s **final vault** after selling *M* policies is:  

$$
\text{Vault}_{\text{end}} = C + M (\pi - \lambda p)
$$  

The **expected yield** is:  

$$
\text{Yield} = \frac{M (\pi - \lambda p)}{C} \times 100\%
$$

---

## 3. Break-Even Condition  
The **break-even probability** *p** occurs when:  

$$
\pi = \lambda p^* \Rightarrow p^* = \frac{\pi}{\lambda}
$$  

- If *p* < *p*: The investor expects a **profit**.  
- If *p* > *p*: The investor expects a **loss**.  

---

## 4. Sample Yields  

### **Assumptions**:  
- **Initial Capital**: *C* = 100,000  
- **Number of Policies**: *M* = 10,000  
- **Premium**: π = 10  
- **Payout per Delay**: λ = 100  

1. **At *p* = 1%**:  

$$
\text{Yield} = \frac{10,000 \times (10 - 100 \times 0.01)}{100,000} = 90\%
$$  

2. **At *p* = 20%**:  

$$
\text{Yield} = \frac{10,000 \times (10 - 100 \times 0.20)}{100,000} = -100\%
$$  

---

## 5. Increasing Premium  
If the **premium increases to π = 20** while keeping λ = 100:  

1. **At *p* = 1%**:  

$$
\text{Yield} = \frac{10,000 \times (20 - 100 \times 0.01)}{100,000} = 190\%
$$  

2. **At *p* = 20% (Break-Even)**:  

$$
\text{Yield} = 0\%
$$  

---

## 6. Yield at 5% Delay, π = 20, λ = 100  
With π = 20, λ = 100, and *p* = 5%:  

$$
\text{Yield} = \frac{10,000 \times (20 - 100 \times 0.05)}{100,000} = 150\%
$$  

---

## 7. Monte Carlo Analysis  
Instead of assuming a **fixed** *p*, simulate underwriting with a **random** *p* drawn from **1% to 20%**:  

1. **Step 1**: Draw *p* randomly over many trials.  
2. **Step 2**: Simulate *M* policies per trial, tallying premiums and payouts.  
3. **Step 3**: Compute the **distribution of yields** over all trials.  
4. **Step 4**: Extract metrics like **expected return, volatility, and worst-case losses**.  

Monte Carlo helps assess **expected profitability and tail risks**.  

---

## 8. Key Observations  
- **Higher premium (π)** increases expected yield and shifts the break-even probability **upward**.  
- **Higher payout (λ)** reduces tolerance for higher *p*.  
- **Increasing policies (*M*)** amplifies potential gains **and** losses.  
- **Larger initial capital (*C*)** does not change absolute profit/loss but **reduces percentage swings**.  

---

## 9. Balancing Risk and Return  
- **Maximizing expected yield** favors **high π and high *M***.  
- Real-world underwriting must consider **worst-case losses** (tail risk).  
- Monte Carlo simulations help select **optimal strategies** balancing **profitability and risk tolerance**.  

--- 

**Note**: All equations use MathJax; Greek symbols (π, λ) are rendered in Unicode for readability.

---

# Flight-Delay Insurance Underwriting Highlights  

## 1. Introduction / Setup  
> *“In this flight-delay insurance model, the investor collects a premium (π) for each policy sold and pays out λ if the flight is delayed. The delay probability, p, varies from **1% to 20%**. We aim to estimate how the investor’s yield shifts when premium, payout, the number of policies (M), and initial capital (C) change.”*  

---

## 2. Key Formula  
The **expected yield** is defined as:  

$$  
\mathbb{E}[\text{Yield}] = \frac{M (\pi - \lambda p)}{C} \times 100\%  
$$  

- \(M\): Number of policies  
- \(π\): Premium per policy  
- \(λ\): Payout per delay  
- \(p\): Probability of delay  
- \(C\): Initial capital  

---

## 3. Yield Ranges  
For π = \$10, λ = \$100, M = 10,000, and C = \$100k:  

| Delay Probability (p) | Yield       |  
|------------------------|-------------|  
| **1%**                 | **+90%**    |  
| **20%**                | **-100%**   |  

---

## 4. Maximizing Yield  
Increasing the premium to **π = \$20** (with λ = \$100 and M = 10,000):  

| Delay Probability (p) | Yield       |  
|------------------------|-------------|  
| **1%**                 | **+190%**   |  
| **5%**                 | **+150%**   |  

---

## 5. Break-Even Probability  
The break-even condition is:  

$$  
\pi = \lambda p^* \quad \Rightarrow \quad p^* = \frac{\pi}{\lambda}  
$$  

**Example**:  
- For π = \$10 and λ = \$100: **p* = 10%**  
- Higher π or lower λ **raises the break-even threshold**.  

---

## 6. Strategic Tradeoffs  
> *“An ‘optimal’ strategy balances high expected yield with acceptable worst-case losses. Selling more policies (M) or charging higher premiums (π) can amplify returns but also heightens risk if delays surge.”*  

**Key levers**:  
- 🚀 **High M/π**: Amplifies gains (and losses).  
- ⚖️ **Balancing**: Use Monte Carlo simulations to model tail risks.  

---

## 7. Final Takeaway  
> *“In practice, weigh potential profits at low delay probabilities against catastrophic losses if delays spike. Monte Carlo simulations help optimize premiums/payouts to balance returns and tail risks.”*  

---

**Note**:  
- Equations use MathJax; Greek symbols (π, λ) are Unicode.  
- Highlighted values (e.g., **+190%**) emphasize critical insights.  