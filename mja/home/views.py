from django.http import HttpResponse
from django.conf import settings
from amadeus import Client, ResponseError

amadeus = Client(
    client_id=settings.AMADEUS_API_KEY,
    client_secret=settings.AMADEUS_API_SECRET
)

def flight_search_view(request):
    html = """
    <html>
    <head><title>✈️ Flight Search</title></head>
    <body>
        <h2>ফ্লাইট সার্চ করুন</h2>
        <form method="get">
            From: <input type="text" name="from"><br><br>
            To: <input type="text" name="to"><br><br>
            Date: <input type="date" name="date"><br><br>
            <button type="submit">Search</button>
        </form>
    """

    if request.method == 'GET' and 'from' in request.GET:
        origin = request.GET.get('from')
        destination = request.GET.get('to')
        departure_date = request.GET.get('date')

        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin,
                destinationLocationCode=destination,
                departureDate=departure_date,
                adults=1
            )
            flights = response.data

            html += "<h3>রেজাল্ট:</h3>"
            for flight in flights:
                segment = flight['itineraries'][0]['segments'][0]
                price = flight['price']['total']
                currency = flight['price']['currency']
                html += f"""
                    <div style="border:1px solid #ccc; margin:10px; padding:10px;">
                        <strong>From:</strong> {segment['departure']['iataCode']}<br>
                        <strong>To:</strong> {segment['arrival']['iataCode']}<br>
                        <strong>Price:</strong> {price} {currency}
                    </div>
                """
        except ResponseError as error:
            html += f"<p style='color:red;'>Error: {str(error)}</p>"

    html += "</body></html>"
    return HttpResponse(html)
