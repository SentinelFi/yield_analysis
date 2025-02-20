# Flight-Delay Insurance Preliminary Yield Analysis

## 1. Introduction

In this model, an investor collects a **premium** (\(\pi\)) for each flight-delay policy sold.  
If a flight is **delayed**, the investor pays a **payout** (\(\lambda\)).  
The probability of delay, \(p\), varies from **1% to 20%**.  
This report estimates how **yield** changes when we adjust premium, payout, the number of policies, and initial capital.

## 2. Yield Formula

The investor’s **final vault** after selling \(M\) policies is:

\[
\text{Vault}_{\text{end}} = C + M \bigl(\pi - \lambda p \bigr).
\]

The **expected yield** is:

\[
\mathbb{E}[\text{Yield}] = \frac{M (\pi - \lambda p)}{C} \times 100\%.
\]

## 3. Break-Even Condition

The **break-even probability** \(p^*\) occurs when:

\[
\pi = \lambda p^* \Rightarrow p^* = \frac{\pi}{\lambda}.
\]

- If \(p < p^*\), the investor expects a **profit**.  
- If \(p > p^*\), the investor expects a **loss**.  

## 4. Sample Yields

### **Assume:**
- **Initial Capital**: \(C = 100,000\)
- **Number of Policies**: \(M = 10,000\)
- **Premium**: \(\pi = 10\)
- **Payout per delay**: \(\lambda = 100\)

1. **At \(p = 1\%\):**

\[
\mathbb{E}[\text{Yield}] = \frac{10,000 \times (10 - 100 \times 0.01)}{100,000} = 90\%.
\]

2. **At \(p = 20\%\):**

\[
\mathbb{E}[\text{Yield}] = \frac{10,000 \times (10 - 100 \times 0.20)}{100,000} = -100\%.
\]

## 5. Increasing Premium

If we **increase the premium** to \(\pi = 20\) while keeping \(\lambda = 100\):

1. **At \(p = 1\%\):**

\[
\mathbb{E}[\text{Yield}] = \frac{10,000 \times (20 - 100 \times 0.01)}{100,000} = 190\%.
\]

2. **At \(p = 20\%\) (Break-even):**

\[
\mathbb{E}[\text{Yield}] = 0\%.
\]

## 6. Yield at 5% Delay, $20 Premium, $100 Payout

With \(\pi = 20\), \(\lambda = 100\), and \(p = 5\%\):

\[
\mathbb{E}[\text{Yield}] = \frac{10,000 \times (20 - 100 \times 0.05)}{100,000} = 150\%.
\]

## 7. Monte Carlo Analysis

Instead of assuming a **fixed** \(p\), we simulate underwriting with a **random** \(p\) drawn from **1% to 20%**:

- **Step 1**: Draw \(p\) randomly over many trials.  
- **Step 2**: Simulate \(M\) policies per trial, tallying premiums and payouts.  
- **Step 3**: Compute the final **distribution of yields** over all trials.  
- **Step 4**: Extract metrics like **expected return, volatility, and worst-case losses**.

Monte Carlo helps assess **expected profitability and tail risks**.

## 8. Key Observations

- **Higher premium (\(\pi\))** increases expected yield and shifts the break-even probability **upward**.
- **Higher payout (\(\lambda\))** reduces profitability tolerance to higher \(p\).
- **Increasing policies (\(M\))** amplifies both potential gains **and** losses.
- **Larger initial capital (\(C\))** does not change absolute profit/loss but **reduces percentage swings**.

## 9. Balancing Risk and Return

- **Maximizing expected yield** favors **high \(\pi\) and high \(M\)**.
- However, **real-world underwriting must consider** **worst-case losses** (tail risk).
- Monte Carlo simulations help select **optimal strategies** balancing **profitability and risk tolerance**.
