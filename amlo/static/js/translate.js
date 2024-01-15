// Function to update subtitle based on language
function updateSubtitle(language) {
    if (language === "en") {
        document.getElementById("home").innerText = "Home";
        document.getElementById("about").innerText = "About";
        document.getElementById("contact").innerText = "Contact";
        document.getElementById("shop").innerText = "Shop";

        
        document.getElementById("sub-head").innerText = "Amlo & Honey";
        document.getElementById("sub-title").innerText = "Delicious natural ingredients";
        
        
        document.querySelector("html").setAttribute("lang", "en");
    } else if (language === "ar") {
        document.getElementById("home").innerText = "رئيسي";
        document.getElementById("about").innerText = "من نحن";
        document.getElementById("contact").innerText = "اتصل بنا";
        document.getElementById("shop").innerText = "متجر";

        document.getElementById("sub-head").innerText = "أملو &العسل";
        document.getElementById("sub-title").innerText = "مكونات طبيعية لذيذة";


        document.querySelector("html").setAttribute("lang", "ar");
    }


    // Save the selected language in localStorage
    localStorage.setItem("selectedLanguage", language);
    localStorage.setItem("storedLanguage_lab", (language === "en" ? "English" : "العربية"));

    document.getElementById("language").innerText = localStorage.getItem("storedLanguage_lab");
}

// Event listener for the "language" element click
document.getElementById("language").addEventListener("click", function () {
    var currentLanguage = this.getAttribute("language");

    // Toggle between English and Arabic
    var newLanguage = (currentLanguage === "en") ? "ar" : "en";
    
    // Update the language attribute and text content
    this.setAttribute("language", newLanguage);
    this.innerText = (newLanguage === "en") ? "English" : "العربية";

    // Update the subtitle based on the new language
    updateSubtitle(newLanguage);
});

// Check if there's a stored language preference in localStorage
var storedLanguage = localStorage.getItem("selectedLanguage");

// If a language is stored, update the UI with the stored language
if (storedLanguage) {
    document.getElementById("language").setAttribute("language", storedLanguage);
    updateSubtitle(storedLanguage);
} else {
    // If no stored language preference, set default to Arabic
    updateSubtitle("ar");
}
