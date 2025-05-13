console.log('This is JS from your About page.')
fetch("/api/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-CSRFToken": getCookie("csrftoken"),  // getCookie تابعەیە کە توکینەکە دەخواتەوە
  },
  body: JSON.stringify(data),
});
