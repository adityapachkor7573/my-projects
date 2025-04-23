document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contactForm");
    const popupOverlay = document.getElementById("popupOverlay");
    const popupWindow = document.getElementById("popupWindow");
    const closePopupButton = document.getElementById("closePopupButton");
    const popupMessage = document.getElementById("popupMessage");

    if (contactForm) {
        contactForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const formData = {
                name: contactForm.name.value,
                email: contactForm.email.value,
                message: contactForm.message.value
            };

            try {
                const response = await fetch("http://localhost:5000/contact", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(formData)
                });

                let responseData = {};

                try {
                    responseData = await response.json(); // <-- Might fail if response isn't valid JSON
                } catch (jsonErr) {
                    console.error("JSON parse error:", jsonErr);
                    throw new Error("Invalid JSON response from server");
                }

                console.log("Server response:", responseData);

                if (response.ok && responseData.success) {
                    // Show success popup
                    if (popupMessage) popupMessage.textContent = responseData.message;
                    popupOverlay.style.display = "block";
                    popupWindow.style.display = "block";
                    contactForm.reset();
                } else {
                    alert("Server error: " + (responseData.error || "Something went wrong."));
                }
            } catch (error) {
                console.error("Fetch failed:", error);
                alert("Failed to send message. Please check your internet connection or try again later.");
            }
        });
    }

    if (closePopupButton) {
        closePopupButton.addEventListener("click", function () {
            popupOverlay.style.display = "none";
            popupWindow.style.display = "none";
        });
    }
});
