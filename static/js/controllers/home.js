'use strict';

angular.module('app')
    .controller('HomeCtrl', function ($scope, $http, $location, apiService) {

        var GRAV_SIZE = 40;

        apiService.getUser().then(function (data){
            data.image_url = $scope.buildGravatarURL(data.email, GRAV_SIZE);
            $scope.user = data;
        }, function (){
            $location.path('/');
        });

        apiService.getEntries().then(function(data){
            $scope.entries = data.entries;
        });

        $scope.logout = function () {
            apiService.postLogout().then(function(){
                $location.path('/');
            });
        };

        $scope.buildGravatarURL = function (email, size) {
            var url = 'http://www.gravatar.com/avatar/';
            url += hex_md5(email);
            url += '?s=' + size;
            return url;
        };
    });