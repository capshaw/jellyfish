'use strict';

var client = angular.module('client', []);

client.config(function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: 'partials/home.html',
            controller: 'HomeCtrl'
        }).
        otherwise({
            redirectTo: '/'
        });
});