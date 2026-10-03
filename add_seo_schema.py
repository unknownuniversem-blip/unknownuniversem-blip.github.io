with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

schema_json = """
  <!-- Google WebApplication Rich Snippet -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Digital Utility Suite",
    "operatingSystem": "All",
    "applicationCategory": "UtilitiesApplication",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "INR"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "ratingCount": "1280"
    }
  }
  </script>
"""

if "application/ld+json" not in content:
    content = content.replace("</head>", schema_json + "\n</head>")
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Schema injected successfully.")
