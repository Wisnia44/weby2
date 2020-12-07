using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Mime;
using System.Threading.Tasks;
using FilesWebDepot.Logic;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace FilesWebDepot.Controllers
{
    [Route("api/files")]
    [ApiController]
    public class FilesController : ControllerBase
    {
        private const string ContentTypeFile = "application/octet-stream";

        private readonly FilesLogic _filesLogic;

        public FilesController(FilesLogic filesLogic)
        {
            _filesLogic = filesLogic;
        }

        // GET: api/<FilesController>
        [HttpGet]
        public IActionResult Get()
        {
            return Ok();
        }

        // GET api/<FilesController>/5
        [HttpGet("{id}")]
        public async Task<IActionResult> Get(string id)
        {
            var result = await _filesLogic.DownloadFile(id);

            return result.IsSuccess
                ? File(result.Value, ContentTypeFile)
                : (IActionResult) NotFound(result.Error);
        }

        // POST api/<FilesController>
        [HttpPost]
        [ProducesResponseType(StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status400BadRequest)]
        public async Task<ActionResult<string>> UploadFile([FromForm] IFormFile file)
        {
            //if (!files.Any()) return BadRequest("No files provided.");

            var result = await _filesLogic.UploadFile(file);
            
            return result.IsSuccess
                ? Ok(result.Value)
                : (ActionResult<string>) BadRequest();
        }

        // PUT api/<FilesController>/5
        [HttpPut("{id}")]
        public IActionResult Put(int id, [FromBody] string value)
        {
            return Ok();
        }

        // DELETE api/<FilesController>/5
        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            return Ok();
        }
    }
}
