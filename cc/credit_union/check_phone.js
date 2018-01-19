"use strict";

var log4js = require('log4js');
var logger = log4js.getLogger();
var request = require('request');

module.exports = {

    metadata: function metadata() {
        return {
            "name": "CheckPhone",
            "properties": {
                "phoneNumber": { "type": "string", "required": true }
            },
            "supportedActions": [ "valid", "invalid" ]
        };
    },

    invoke: (conversation, done) => {
        var phoneNumber = conversation.properties().phoneNumber;
        logger.debug('CheckPhone: checking for user with phone number: ' + phoneNumber);

        var options = { 
            method: 'GET',
            url: 'http://129.146.81.61:8080/check_mobile?mobile=' + phoneNumber,
        };

        request(options, function (err, res, body) {
            if (err) throw new Error(err);
            console.log(body);
            var data = JSON.parse(body);
            if (data.success) {
                var name = data.user["name"].split(" ");
                var first = name[0];
                var last = name[1];
                var addresses = data.addresses[0];
                for (var i=1; i<data.addresses.length; i++) {
                    addresses += ", " + data.addresses[i];
                }
                conversation.variable("addresses", addresses);
                conversation.variable("profile.firstName", first);
                conversation.variable("profile.lastName", last);
                conversation.variable("validAuthCode", data.user["authCode"]);
                conversation.variable("validAddress", data.user["address"]);
                conversation.transition("valid");
            } else {
                conversation.transition("invalid");
            }
            done();
        });
    }
};
