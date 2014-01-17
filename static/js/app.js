'use strict';

var app = angular.module('app', ['infinite-scroll']);

app.config(function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/static/partials/loading.html',
            controller: 'LoadingCtrl'
        }).
        when('/login', {
            templateUrl: '/static/partials/login.html',
            controller: 'LoginCtrl'
        }).
        when('/home', {
            templateUrl: '/static/partials/home.html',
            controller: 'HomeCtrl'
        }).
        when('/add', {
            templateUrl: '/static/partials/add.html',
            controller: 'AddCtrl'
        }).
        when('/edit/:entryId', {
            templateUrl: '/static/partials/add.html',
            controller: 'AddCtrl'
        }).
        when('/settings', {
            templateUrl: '/static/partials/settings.html',
            controller: 'SettingsCtrl'
        }).
        otherwise({
            redirectTo: '/home'
        });
});