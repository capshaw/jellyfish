'use strict';

angular.module('mainApp')
    .controller('AddCtrl', function ($scope, $http, apiService, $location,
        $routeParams) {

        // When 'add,' content is empty to begin with. Otherwise, load the
        // content from the backend.
        $scope.content = '';
        if ('entryId' in $routeParams) {
            $scope.entryId = $routeParams.entryId;
            apiService.getEntry($scope.entryId).then(function(data){
                $scope.content = data.content;
                $scope.edit = true;
            });
        }

        var converter = new Showdown.converter();

        $scope.markdown = function (input) {
            return converter.makeHtml(input);
        };

        $scope.saveEntry = function () {
            if ($scope.edit) {
                $scope.updateEntry();
            } else {
                $scope.postEntry();
            }
        };

        $scope.postEntry = function () {
            apiService.postEntry($scope.content).then(function(){
                $location.path('/');
            });
        };

        $scope.updateEntry = function () {
            apiService.updateEntry($scope.entryId, $scope.content).then(
                function(){
                $location.path('/');
            })
        };
    });