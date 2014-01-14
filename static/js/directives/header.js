'use strict';

angular.module('app')
    .controller('HeaderCtrl', function($scope, $location, apiService) {

        var GRAV_SIZE = 40;

        // The user must be signed in to be on any page with a header.
        apiService.getUser().then(function (data){
            data.image_url = $scope.buildGravatarURL(data.email, GRAV_SIZE);
            $scope.user = data;
        }, function (){
            $location.path('/');
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
    })
    .directive('header', function() {
        return {
            restrict: 'E',
            scope: {},
            controller: 'HeaderCtrl',
            templateUrl: '/static/partials/header.html'
        };
    });