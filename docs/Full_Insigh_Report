# 📊 Full Insights Report – Revolut Financial Crime Dashboard

**Period covered:** 2019-W13 to 2019-W19  
**Data sources:** `transactions.csv`, `users.csv`, `fraudsters.csv` (processed into `base_2_202508041440.csv`)  
**Granularity:** Weekly (ISO weeks), amounts in GBP  

---

## 1. Overview

This report presents a detailed analysis of user activity, transaction patterns, and fraud trends observed in the covered period. The goal is to extract actionable insights for Fraud Prevention, Compliance, and Risk Management teams.

The dashboard enables both a **macro-level view** (KPIs, aggregated patterns) and **micro-level drill-downs** (transaction type, country, week).

---

## 2. Key Metrics

| Metric                 | Value              |
|------------------------|--------------------|
| Active users           | 482,810            |
| Transactions           | 1,068,361          |
| Total volume           | £36,417,924        |
| Fraud rate             | 0.77%              |
| Fraudulent amount      | ~£281,417          |
| Observation window     | 7 weeks            |

---

## 3. Fraud Trend Analysis

### 3.1 Weekly Evolution
- **Peak**: Weeks **W14–W15**, with ~£130k/week in fraudulent amounts.
- **Post-peak decline**: Progressive reduction after W15, suggesting:
  - Potential effectiveness of new detection rules.
  - Seasonal or event-driven fraud spikes.

**Recommendation:**  
Perform a root-cause analysis of the W14–W15 surge to confirm whether it was triggered by:
- External events (e.g., public holidays, marketing campaigns).
- Exploitation of a system loophole later patched.
- Fraud migration from another channel.

---

## 4. Transaction Type Analysis

### 4.1 Volume distribution
- **TOPUP** dominates both total transaction volume and fraudulent transaction count.
- Other common types: CARD_PAYMENT, TRANSFER, ATM, EXCHANGE.

### 4.2 Fraud concentration
- Fraud rate highest in **TOPUP** operations.
- Possible reasons:
  - Lower friction or verification in funding events.
  - Use of stolen credentials/cards to inject funds.

**Recommendation:**  
- Apply velocity checks on repeat top-ups within short timeframes.
- Add KYC verification layers for large or unusual top-up amounts.
- Monitor the origin of funds (bank accounts, cards, external wallets).

---

## 5. Geographic Analysis

### 5.1 Fraud hotspots
- **Ireland (IE)** and **Cyprus (CY)** rank highest in both fraudulent amounts and transaction counts.
- Gap with next countries is significant.

### 5.2 Possible drivers
- Jurisdiction-specific vulnerabilities.
- Regulatory or enforcement gaps.
- Coordinated fraud rings targeting these markets.

**Recommendation:**  
- Implement **market-specific rules** for IE and CY (stricter authentication, additional document checks).
- Increase fraud analyst coverage for these markets.
- Engage with local authorities for intelligence sharing.

---

## 6. Operational Implications

### Short-term actions
1. **Enhance TOPUP controls** (source-of-funds, velocity limits, enhanced due diligence).
2. **Deploy targeted rules** for IE and CY.
3. **Automate weekly anomaly detection** for fraud rate spikes.

### Medium-term actions
4. **Integrate behavioural analytics** to detect unusual transaction sequences.
5. **Refine alert prioritisation** to focus on high-value/high-risk transactions.
6. **Conduct quarterly hotspot reviews** to adjust controls per country.

---

## 7. Next Steps for the Dashboard

- **Real-time monitoring**: Integrate streaming data to move from weekly to daily/hourly resolution.
- **Drill-down capabilities**: Add per-user fraud timelines for investigation.
- **Link analysis**: Visualise connections between fraudulent accounts and transactions.
- **Alert export**: Enable CSV/PDF export for case management systems.

---

## 8. Conclusion

The analysis confirms that:
- Fraud is concentrated in **specific transaction types (TOPUP)** and **specific geographies (IE, CY)**.
- There is a temporal component, with a notable spike in W14–W15.
- Focused interventions in these areas can yield the highest impact.

Maintaining and refining this dashboard will allow Revolut’s fraud teams to **move faster from detection to prevention**, optimising both security and customer experience.

---
