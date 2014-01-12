'use strict';

angular.module('app')
    .controller('LoginCtrl', function ($scope, $http, $location, apiService) {

        apiService.getUser().then(function (data){
            $location.path('/home');
        });

        $scope.attemptLogin = function () {
            $scope.attemptingLogin = true;

            var data = {
                email: $scope.email,
                password: $scope.password
            }
            $http({method: 'POST', url: '/login', data: data}).
                success(function(data, status, headers, config) {
                    $scope.attemptingLogin = false;
                    $location.path('/home');
                }).
                error(function(data, status, headers, config) {
                    $scope.attemptingLogin = false;
                    $scope.failedLogin = true;
                });
        }

    });