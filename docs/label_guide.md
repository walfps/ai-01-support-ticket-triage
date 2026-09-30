# Label Guide: Support Ticket Triage

## User story
The lead support person gets many customer messages every day. Sorting them
by hand into the right team takes a lot of time. The app reads each message,
suggests one category and a draft reply, and shows how sure it is. The lead
support person checks the suggestion, fixes it if it is wrong, and confirms it.
The app never sends anything to a customer by itself.

## Categories
Every ticket gets exactly one label.

### billing
Problems with money: charges, payments, invoices, prices.
- I got charged twice.
- I can't download the invoice.
- My card was charged the wrong amount.
- The price on my bill is different from the website.

### delivery
Problems with getting the order: late, missing, damaged or wrong item.
- My package still not received.
- My package arrived damaged.
- I got the wrong package.
- The tracking page shows no update for a week.

### technical
Problems with the website or the app: login, errors, pages that do not work.
- The reset-password page doesn't open.
- I can't log in to my account.
- The app closes when I open my orders.
- The website shows an error on my orders page.

### other
No single clear category, or a person must decide.
- Refund my order please.
- I was charged twice and my package never arrived.
- This is the worst service ever!!!
- Do you have a store in my city?

## Tricky cases
| Message | Label | Rule | Why |
|---|---|---|---|
| Refund my order please | other | Refund requests are decided by a person | A refund can involve money and delivery, so a person decides |
| I was charged twice and my package never arrived | other | Two problems in one message go to other | It belongs to two teams, so a person decides who goes first |
| This is the worst service ever!!! | other | Angry message with no clear problem goes to other, and the lead support person reviews it | There is no problem to route yet |

## Out of scope
- The app does not send replies to customers by itself.
- The app does not give refunds or take payments.
- English messages only.