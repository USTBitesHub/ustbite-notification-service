def order_confirmed_email(
    user_name: str,
    restaurant_name: str,
    order_id: str,
    items: list,
    total: float,
    floor: str,
    wing: str,
    estimated_minutes: int,
    frontend_url: str
) -> dict:
    items_html = "".join([
        f"""
        <tr>
          <td style="padding:8px;border-bottom:
            1px solid #E5E7EB;">{item['name']}</td>
          <td style="padding:8px;border-bottom:
            1px solid #E5E7EB;
            text-align:center;">x{item.get('qty', item.get('quantity', 1))}</td>
          <td style="padding:8px;border-bottom:
            1px solid #E5E7EB;
            text-align:right;">
            ₹{item['price']}</td>
        </tr>
        """
        for item in items
    ])

    html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;
      font-family:Inter,Arial,sans-serif;
      background:#F9F5F0;">
      <div style="max-width:600px;margin:40px auto;
        background:#ffffff;border-radius:8px;
        overflow:hidden;
        box-shadow:0 2px 8px rgba(0,0,0,0.08);">

        <!-- Header -->
        <div style="background:#1C1C1E;padding:24px 32px;
          border-top:4px solid #F59E0B;">
          <h1 style="color:#ffffff;margin:0;
            font-size:24px;font-weight:700;">
            USTBite
          </h1>
          <p style="color:#9CA3AF;margin:4px 0 0;">
            Your UST cafeteria, delivered to your floor
          </p>
        </div>

        <!-- Body -->
        <div style="padding:32px;">
          <h2 style="color:#1C1C1E;margin:0 0 8px;">
            Order Confirmed! 🎉
          </h2>
          <p style="color:#6B7280;margin:0 0 24px;">
            Hi {user_name}, your order from 
            <strong>{restaurant_name}</strong> 
            is confirmed and being prepared.
          </p>

          <!-- Order Details -->
          <div style="background:#F9F5F0;
            border-radius:8px;padding:20px;
            margin-bottom:24px;">
            <p style="margin:0 0 4px;color:#6B7280;
              font-size:12px;text-transform:uppercase;
              letter-spacing:0.05em;">Order ID</p>
            <p style="margin:0 0 16px;color:#1C1C1E;
              font-weight:600;font-family:monospace;">
              {order_id}
            </p>
            <p style="margin:0 0 4px;color:#6B7280;
              font-size:12px;text-transform:uppercase;
              letter-spacing:0.05em;">
              Delivering To
            </p>
            <p style="margin:0;color:#1C1C1E;
              font-weight:600;">
              Floor {floor}, Wing {wing}
            </p>
          </div>

          <!-- Items Table -->
          <table style="width:100%;
            border-collapse:collapse;
            margin-bottom:16px;">
            <thead>
              <tr style="background:#F9F5F0;">
                <th style="padding:8px;text-align:left;
                  color:#6B7280;font-size:12px;">
                  Item</th>
                <th style="padding:8px;text-align:center;
                  color:#6B7280;font-size:12px;">
                  Qty</th>
                <th style="padding:8px;text-align:right;
                  color:#6B7280;font-size:12px;">
                  Price</th>
              </tr>
            </thead>
            <tbody>
              {items_html}
            </tbody>
          </table>

          <!-- Total -->
          <div style="text-align:right;
            padding:12px 0;
            border-top:2px solid #1C1C1E;">
            <span style="font-size:18px;
              font-weight:700;color:#1C1C1E;">
              Total: ₹{total}
            </span>
          </div>

          <!-- Estimated Time -->
          <div style="background:#FEF3C7;
            border-left:4px solid #F59E0B;
            padding:12px 16px;border-radius:4px;
            margin:24px 0;">
            <p style="margin:0;color:#92400E;
              font-weight:600;">
              ⏱ Estimated delivery: 
              {estimated_minutes} minutes
            </p>
          </div>

          <!-- Track Button -->
          <div style="text-align:center;
            margin-top:24px;">
            <a href="{frontend_url}/orders/{order_id}"
              style="background:#F59E0B;
              color:#1C1C1E;padding:14px 32px;
              border-radius:6px;
              text-decoration:none;
              font-weight:700;font-size:16px;
              display:inline-block;">
              Track My Order
            </a>
          </div>
        </div>

        <!-- Footer -->
        <div style="background:#F9F5F0;
          padding:20px 32px;text-align:center;
          border-top:1px solid #E5E7EB;">
          <p style="margin:0;color:#9CA3AF;
            font-size:12px;">
            © 2026 USTBite · UST Campus Cafeteria Platform
          </p>
        </div>

      </div>
    </body>
    </html>
    """
    return {
        "subject": f"Order Confirmed — {restaurant_name} 🍽️",
        "html": html
    }


def order_delivered_email(
    user_name: str,
    restaurant_name: str,
    order_id: str,
    floor: str,
    wing: str
) -> dict:
    html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;
      font-family:Inter,Arial,sans-serif;
      background:#F9F5F0;">
      <div style="max-width:600px;margin:40px auto;
        background:#ffffff;border-radius:8px;
        overflow:hidden;
        box-shadow:0 2px 8px rgba(0,0,0,0.08);">

        <div style="background:#1C1C1E;padding:24px 32px;
          border-top:4px solid #F59E0B;">
          <h1 style="color:#ffffff;margin:0;
            font-size:24px;font-weight:700;">
            USTBite
          </h1>
        </div>

        <div style="padding:32px;text-align:center;">
          <div style="font-size:64px;margin-bottom:16px;">
            🎉
          </div>
          <h2 style="color:#1C1C1E;margin:0 0 8px;">
            Your order has been delivered!
          </h2>
          <p style="color:#6B7280;
            margin:0 0 24px;font-size:16px;">
            Hi {user_name}, your order from 
            <strong>{restaurant_name}</strong> 
            has arrived at 
            <strong>Floor {floor}, Wing {wing}</strong>.
          </p>
          <p style="color:#6B7280;margin:0;
            font-size:15px;">
            Enjoy your meal! 🍽️
          </p>
          <p style="color:#9CA3AF;margin:16px 0 0;
            font-size:13px;font-family:monospace;">
            Order ID: {order_id}
          </p>
        </div>

        <div style="background:#F9F5F0;
          padding:20px 32px;text-align:center;
          border-top:1px solid #E5E7EB;">
          <p style="margin:0;color:#9CA3AF;
            font-size:12px;">
            © 2026 USTBite · UST Campus Cafeteria Platform
          </p>
        </div>
      </div>
    </body>
    </html>
    """
    return {
        "subject": "Delivered! Enjoy your meal 🎉",
        "html": html
    }


def payment_failed_email(
    user_name: str,
    amount: float,
    order_id: str,
    frontend_url: str
) -> dict:
    html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;
      font-family:Inter,Arial,sans-serif;
      background:#F9F5F0;">
      <div style="max-width:600px;margin:40px auto;
        background:#ffffff;border-radius:8px;
        overflow:hidden;
        box-shadow:0 2px 8px rgba(0,0,0,0.08);">

        <div style="background:#1C1C1E;padding:24px 32px;
          border-top:4px solid #DC2626;">
          <h1 style="color:#ffffff;margin:0;
            font-size:24px;font-weight:700;">
            USTBite
          </h1>
        </div>

        <div style="padding:32px;">
          <h2 style="color:#DC2626;margin:0 0 8px;">
            Payment Failed
          </h2>
          <p style="color:#6B7280;margin:0 0 24px;">
            Hi {user_name}, we were unable to process 
            your payment of 
            <strong>₹{amount}</strong> 
            for order <code>{order_id}</code>.
          </p>
          <p style="color:#6B7280;margin:0 0 24px;">
            Please try placing your order again 
            with a different payment method.
          </p>
          <div style="text-align:center;">
            <a href="{frontend_url}/restaurants"
              style="background:#F59E0B;
              color:#1C1C1E;padding:14px 32px;
              border-radius:6px;
              text-decoration:none;
              font-weight:700;font-size:16px;
              display:inline-block;">
              Try Again
            </a>
          </div>
        </div>

        <div style="background:#F9F5F0;
          padding:20px 32px;text-align:center;
          border-top:1px solid #E5E7EB;">
          <p style="margin:0;color:#9CA3AF;
            font-size:12px;">
            © 2026 USTBite · UST Campus Cafeteria Platform
          </p>
        </div>
      </div>
    </body>
    </html>
    """
    return {
        "subject": "Payment Failed — Please retry your order",
        "html": html
    }
