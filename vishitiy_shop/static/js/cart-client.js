import { Client } from "/static/js/client.js";

export class CartClient {

    constructor() {
        this.url = window.location.origin + '/cart/';
        this.client = new Client(); 
    }

    _remove(e, data) {
        e.target.closest('.item').remove();
    }

    remove(e) {
        e.preventDefault();
        const data = new FormData(e.target);
        this.client.sendReq(this.url + 'remove/', 'POST', data, (data) => this._remove(e, data));
    }

    add(e) {
        console.log("CartClient.add()", e);
        e.preventDefault();
        const data = new FormData(e.target);
        this.client.sendReq(this.url + 'add/', 'POST', data, null, 'При додаванні товару сталася помилка. Спробуйте пізніше');
    }
}
