'use strict';

angular.module('app')
    .controller('EntryCtrl', function($scope, apiService) {

        var converter = new Showdown.converter();

        $scope.markdown = function (input) {
            return converter.makeHtml(input);
        };

        $scope.deleteEntry = function (id, index) {
            apiService.deleteEntry(id).then(function(){
                $scope.deleted = true;
            })
        };
    })
    .directive('entry', function() {
        return {
            restrict: 'E',
            scope: {
                entry: '=entry'
            },
            controller: 'EntryCtrl',
            templateUrl: '/static/partials/entry.html'
        };
    });