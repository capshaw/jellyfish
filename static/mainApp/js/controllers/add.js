'use strict';

angular.module('mainApp')
    .controller('AddCtrl', function ($scope, $http, apiService, $location) {

        $scope.content = '';

        var converter = new Showdown.converter();

        $scope.markdown = function (input) {
            return converter.makeHtml(input);
        };

        $scope.postEntry = function () {
            apiService.postEntry($scope.content).then(function(){
                $location.path('/');
            });
        };
    });