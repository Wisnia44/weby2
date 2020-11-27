using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Abstractions;
using System.Threading.Tasks;
using CSharpFunctionalExtensions;
using FilesWebDepot.Constants;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace FilesWebDepot.Logic
{
    public class FilesLogic
    {
        private readonly IFileSystem _fileSystem;

        public FilesLogic(): this(new FileSystem()){}

        internal FilesLogic(IFileSystem fileSystem)
        {
            _fileSystem = fileSystem;
        }

        public async Task<Result<string>> UploadFile(IFormFile formFile)
        {
            if (formFile.Length == 0)
                return Result.Failure<string>("File is empty.");

            var savedFileName = formFile.FileName;

            var savedFilePath = EnsureDirectoryExists(FilesConstants.ResourcesDirectory)
                .Bind(path => Result.Success(_fileSystem.Path.Join(path, savedFileName)));

            await using (var stream = _fileSystem.FileStream.Create(savedFilePath.Value, FileMode.Create))
            {
                await formFile.CopyToAsync(stream);
            }

            return Result.Success(savedFileName);
        }

        public async Task<Result<Stream>> DownloadFile(string fileId)
        {
            var expectedFilePath = _fileSystem.Path.Join(FilesConstants.ResourcesDirectory, fileId);

            if (!_fileSystem.File.Exists(expectedFilePath)) return Result.Failure<Stream>("File not exists");

            var stream = _fileSystem.FileStream.Create(expectedFilePath, FileMode.Open);
            
            return Result.Success(stream);
        }

        private Result<string> EnsureDirectoryExists(string directoryPath)
        {
            if (_fileSystem.Directory.Exists(directoryPath)) return directoryPath;

            try
            {
                _fileSystem.Directory.CreateDirectory(directoryPath);
            } catch (Exception e)
            {
                Console.WriteLine(e);
                throw;
            }

            return directoryPath;
        }
    }
}
