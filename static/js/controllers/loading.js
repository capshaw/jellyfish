'use strict';

angular.module('app')
    .controller('LoadingCtrl', function ($scope, apiService, $location) {
        apiService.getUser().then(function () {
            $location.path('/home');
        }, function (data){
            $location.path('/login');
        });
    });