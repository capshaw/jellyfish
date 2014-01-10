'use strict';

var mainApp = angular.module('mainApp', []);

mainApp.config(function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/static/mainApp/partials/home.html',
            controller: 'HomeCtrl'
        }).
        when('/add', {
            templateUrl: '/static/mainApp/partials/add.html',
            controller: 'AddCtrl'
        }).
        when('/edit/:entryId', {
            templateUrl: '/static/mainApp/partials/add.html',
            controller: 'AddCtrl'
        }).
        otherwise({
            redirectTo: '/'
        });
});