'use strict';

angular.module('app')
    .controller('HomeCtrl', function ($scope, $http, $location, apiService) {

        var GRAV_SIZE = 40;

        var converter = new Showdown.converter();

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

        // TODO: make this a two-step process.
        $scope.deleteEntry = function (id, index) {
            apiService.deleteEntry(id).then(function(){
                $scope.entries.splice(index, 1);
            })
        };

        $scope.buildGravatarURL = function (email, size) {
            var url = 'http://www.gravatar.com/avatar/';
            url += hex_md5(email);
            url += '?s=' + size;
            return url;
        };

        $scope.markdown = function (input) {
            return converter.makeHtml(input);
        };
    });