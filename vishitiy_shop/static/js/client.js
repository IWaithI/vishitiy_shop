import { showToast } from "/static/js/notifications.js";

export class Client {
    async sendReq(url, method, body, callBack = null, errorMsg = null) {
      try {
        const response = await fetch(url, {
          method: method,
          body: body,
        });
  
        const text = await response.text();
        let data = text ? JSON.parse(text) : {};
        console.log("DATA ZAPROSa", data);
        if (response.ok) {
            if (data.msg) showToast(data.msg)
            if (callBack) callBack(data);
        } else {
            console.error("HTTP Error:", response.status, response.statusText);
            if (data.errors) {
                for (const [key, value] of Object.entries(data.errors)) {
                    showToast(value, "danger");
                }
                return;
            }
            if (data.msg) {
                showToast(data.msg, "danger");
                return;
            }
        } 
    } catch (error) {
        console.error("Error:", error);
        if (errorMsg) {
          showToast(errorMsg, "danger");
        } else {
          showToast("Unexpected error occurred", "danger");
        }
      }
    }
  } 
  