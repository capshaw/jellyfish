'use strict';

angular.module('anonApp')
    .controller('LoginCtrl', function ($scope, $http) {

        $scope.attemptLogin = function () {
            $scope.attemptingLogin = true;

            var data = {
                email: $scope.email,
                password: $scope.password
            }
            $http({method: 'POST', url: '/login', data: data}).
                success(function(data, status, headers, config) {
                    $scope.attemptingLogin = false;
                    window.location.replace('/');
                }).
                error(function(data, status, headers, config) {
                    $scope.attemptingLogin = false;
                    $scope.failedLogin = true;
                });
        }

    });