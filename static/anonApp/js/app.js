'use strict';

var anonApp = angular.module('anonApp', []);

anonApp.config(function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/static/anonApp/partials/login.html',
            controller: 'LoginCtrl'
        }).
        otherwise({
            redirectTo: '/'
        });
});