using System.IO;

namespace FilesWebDepot.Constants
{
    public static class FilesConstants
    {
        private static string ResourcesDirectoryName { get; } = "Resources";

        public static string ResourcesDirectory { get; } = Path.Combine(Directory.GetCurrentDirectory(), ResourcesDirectoryName);
    }
}
