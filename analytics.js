(function () {
  var measurementId = "G-M4Q5BVSD2B";
  var consentKey = "plushtrap_analytics_consent";
  var allowedQueryKeys = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "fbclid", "ttclid"];

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };

  function sanitizedLocation() {
    var url = new URL(window.location.href);
    var allowed = new URLSearchParams();
    allowedQueryKeys.forEach(function (key) {
      var value = url.searchParams.get(key);
      if (value) allowed.set(key, value.slice(0, 200).toLowerCase());
    });
    url.search = allowed.toString();
    url.hash = "";
    return { location: url.toString(), path: url.pathname + url.search };
  }

  function trackPageView() {
    var safe = sanitizedLocation();
    window.gtag("event", "page_view", {
      page_location: safe.location,
      page_path: safe.path,
      page_title: document.title
    });
  }

  window.gtag("consent", "default", {
    analytics_storage: localStorage.getItem(consentKey) === "granted" ? "granted" : "denied",
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    wait_for_update: 500
  });
  window.gtag("js", new Date());
  window.gtag("config", measurementId, {
    send_page_view: false,
    allow_google_signals: false,
    allow_ad_personalization_signals: false
  });
  if (localStorage.getItem(consentKey) === "granted") trackPageView();

  window.plushtrapAnalyticsConsent = function (granted) {
    localStorage.setItem(consentKey, granted ? "granted" : "denied");
    window.gtag("consent", "update", {
      analytics_storage: granted ? "granted" : "denied",
      ad_storage: "denied",
      ad_user_data: "denied",
      ad_personalization: "denied"
    });
    var banner = document.getElementById("analytics-consent");
    if (banner) banner.remove();
    if (granted) trackPageView();
  };

  document.addEventListener("DOMContentLoaded", function () {
    if (localStorage.getItem(consentKey) !== null) return;
    var banner = document.createElement("div");
    banner.id = "analytics-consent";
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-label", "Analytics preferences");
    banner.innerHTML = '<p>Allow anonymous analytics to improve products and checkout? Advertising storage stays disabled.</p><button type="button" onclick="window.plushtrapAnalyticsConsent(true)">Allow analytics</button><button type="button" onclick="window.plushtrapAnalyticsConsent(false)">Decline</button>';
    document.body.appendChild(banner);
  });
})();
