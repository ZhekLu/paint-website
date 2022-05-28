import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {catchError, Observable, of} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class PpService {
  private url: String = 'http://localhost:8000';
  constructor(private http: HttpClient) { }

  getPps(): Observable<Object[]> {
    return this.http.get<Object[]>(this.url + '/api/pps/');
  }

  getPp(pk: Number): Observable<Object> {
    return this.http.get<Object>(this.url + '/api/pps/' + pk);
  }

  handleError() {
    return (error: any): Observable<Object> => {
      window.alert(error.message);
      return of(0);
    }
  }

  addComment(pp: String, author: String, password: String, content: String)
  : Observable<Object> {
    const comment = {'pp': pp, 'author': author, 'content': content};
    const options = {headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + window.btoa(author + ':' + password)
    })};
    return this.http.post<Object>(this.url + '/api/pps/' + pp + '/comments/',
      comment, options).pipe(catchError(this.handleError()));
  }

  getComments(pk: Number): Observable<Object[]> {
    return this.http.get<Object[]>(this.url + '/api/pps/' + pk + '/comments/');
  }
}
